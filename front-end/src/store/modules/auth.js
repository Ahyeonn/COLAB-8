import axios from "axios";

export default {
    state() {
        return {
            isLoggedIn: localStorage.getItem('is-loggedIn'),
            user: {
                name: '',
                phoneNumber: '',
                password: ''
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
        // ADD_EVENT(state, event) {
        //     state.events.push(event)
        // },
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
                    console.log(res.data[0].events)
                    context.commit('UPDATE_USER', user);
                    context.commit('LOG_IN', true);
                    context.commit(`ADD_EVENT`, res.data[0].events)
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
