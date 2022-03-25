import axios from "axios";

export default {
    state() {
        return {
            events: '',
            eventDetails: []
        }
    },
    mutations: {
        ADD_EVENT(state, payload) {
            state.events = payload
        },
        SET_EVENT_DETAILS(state, payload) {
            state.eventDetails = payload
        }
    },
    actions: {
        async fetchEventDetails({commit}, id) {
            await axios.get(`https://colab8.herokuapp.com/api/events/${id}`)
                .then(res => {
                    console.log(res.data);
                    commit('SET_EVENT_DETAILS', res.data)
                })
        }
    }
}
