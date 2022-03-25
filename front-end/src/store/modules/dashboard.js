// import axios from "axios";

export default {
    state() {
        return {
            events: '',
        }
    },
    mutations: {
        ADD_EVENT(state, payload) {
            state.events = payload
        },
    },
    actions: {
        // async fetchEvents({commit}) {
        //     await axios.get('https://colab8.herokuapp.com/api/users/events')
        //         .then(res => {
        //             console.log(res);
        //             commit('ADD_EVENT', res)
        //         })
        // }
    }
}
