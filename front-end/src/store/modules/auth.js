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
                .then(() => {
                    context.commit('UPDATE_USER', user);
                    context.commit('LOG_IN', true);
                })
                .catch(error => {
                    throw error.response.data.error
                })
        },
    }
}
