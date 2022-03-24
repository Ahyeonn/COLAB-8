import axios from "axios";

export default {
    state() {
        return {
            events: [],
        }
    },
    mutations: {
        ADD_EVENT(state, event) {
            state.meetings.push(event)
        },
    },
    actions: {
        async getEvents({commit}) {
            await axios.get('https://colab8.herokuapp.com/api/users/events')
                .then(res => {
                    console.log(res);
                    commit('ADD_EVENT', res)
                })
        }
    }
}
