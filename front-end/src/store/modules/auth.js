import axios from "axios";

export default {
    state() {
        return {
            isLoggedIn: localStorage.getItem('is-loggedIn'),
            user: {
                name: '',
                phoneNumber: '',
                password: ''
            },
            authenticatedUser: {
                id: localStorage.getItem('user_id'),
                name: localStorage.getItem('user_name')
            }
        }
    },
    mutations: {
        UPDATE_USER(state, payload) {
            state.user = Object.assign({}, state.user, payload);
        },
        LOG_IN(state, value) {
            state.isLoggedIn = value;
            localStorage.setItem('is-loggedIn', value);
        },
        SET_AUTHENTICATED_USER(state, payload) {
            state.authenticatedUser = {
                id: payload[0].user_id,
                name: payload[1].user_name,
            }
            localStorage.setItem('user_id', payload[0].user_id);
            localStorage.setItem('user_name', payload[1].user_name);
        }
    },
    actions: {
        async register(context, user) {
            await axios.post('https://colab8.herokuapp.com/api/users/signup', {
                owner_id: null,
                name: user.name,
                phone_number: user.phoneNumber,
                password: user.password,
            })
                .then(() => {
                    context.commit('UPDATE_USER', user);
                })
                .catch(error => {
                    throw error.response.data.error
                })
        },
        async login(context, user) {
            await axios.post('https://colab8.herokuapp.com/api/users/signin', {
                owner_id: null,
                phone_number: user.phoneNumber,
                password: user.password,
            })
                .then((res) => {
                    console.log(res.data[2])
                    const data = res.data
                    context.commit('UPDATE_USER', user);
                    context.commit('LOG_IN', true);
                    context.commit(`ADD_EVENT`, data[0].events)
                    context.commit('SET_AUTHENTICATED_USER', [data[1], data[2]])
                })
                .catch(error => {
                    console.log(error)
                    if (error.response) {
                        throw error.response.data.error
                    }
                })
        },
    }
}
