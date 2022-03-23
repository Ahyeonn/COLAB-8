import { createStore } from 'vuex'
import authModule from "./modules/auth";
import axios from 'axios'

export default createStore({
    // Note: strict mode should turn off in production
    strict: true,
    state: {
        meetings: [],
        meetingMembers: {
            hostMumber: '',
            contacts: []
        }
    },
    getters: {
      getContacts(state) {
          return state.meetingMembers.contacts.map(({name})=>{
               return name
          });
      },
        getMeeting(state) {
              return state.meetings.map(meeting =>{
                  console.log(meeting)
                  return meeting
              });
        }
    },
    mutations: {
        ADD_MEETING(state, meeting) {
            state.meetings.push(meeting)
        },
        ADD_HOST_NUMBER(state, number) {
          state.meetingMembers.hostMumber = number
        },
        ADD_CONTACT(state, contact) {
            state.meetingMembers.contacts.push(contact)
        }
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
