import { createStore } from 'vuex'
import authModule from "./modules/auth";
import axios from 'axios'

export default createStore({
    // Note: strict mode should turn off in production
    strict: true,
    state: {
        meetings: [],
    },
    mutations: {
        ADD_MEETING(state, meeting) {
            state.meetings.push(meeting)
        },
    },
    actions: {
       createMeeting(context, meeting) {
            axios.post('https://colab8.herokuapp.com/api/events/create', {
                owner_id: null,
                name: meeting.hostName,
                event_name: meeting.name,
                date: meeting.date,
                time: meeting.time
            })
                .then(res => {
                    console.log(res.data);
                    context.commit('ADD_MEETING', meeting);
                })
                .catch(error => {
                    console.log(error.response)
                })

        }
    },
    modules: {
        auth: authModule
    }
})
