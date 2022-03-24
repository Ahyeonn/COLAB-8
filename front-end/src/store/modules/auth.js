import axios from "axios";

export default {
    state() {
        return {
            isLoggedIn: false,
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
                })
                .catch(error => {
                    throw error.response.data.error
                })
        },
    }
}
