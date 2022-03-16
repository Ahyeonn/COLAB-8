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
    }
}
