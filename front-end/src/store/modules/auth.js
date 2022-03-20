import axios from "axios";

export default {
    state() {
        return {
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
        }
    },
    actions: {
        register(context, user) {
            axios.post('https://colab8.herokuapp.com/api/users/signup', {
                owner_id: null,
                name: user.name,
                phone_number: user.phoneNumber,
                password: user.password,
            })
                .then(res => {
                    console.log(res.data);
                    context.commit('UPDATE_USER', user);
                })
                .catch(error => {
                    console.log(error.response)
                })
        }
    }
}
