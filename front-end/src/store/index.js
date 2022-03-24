import { createStore } from 'vuex'
import authModule from "./modules/auth";
import dashboardModule from "./modules/dashboard";
import axios from 'axios'

export default createStore({
    // Note: strict mode should turn off in production
    strict: true,
    state: {
        meetings: [],
        meetingMembers: {
            event_id: null,
            contacts: []
        }
    },
    getters: {
      getContacts(state) {
          return state.meetingMembers.contacts.map((contact)=>{
               return contact
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
        ADD_CONTACT(state, contact) {
            state.meetingMembers.contacts.push(contact)
        }
    },
    actions: {
       createMeeting(context, meeting) {
            axios.post('https://colab8.herokuapp.com/api/events/create', {
                event_id: meeting.id,
                owner_id: null,
                name: meeting.hostName,
                host_number : meeting.hostNumber,
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
        },
        sendRecipients(context, meetingMembers) {
            axios.post('https://colab8.herokuapp.com/api/events/rsvp', {
                contacts : meetingMembers,
                event_id : 100
            })
                .then(res => {
                    console.log(res.data);
                    context.commit('ADD_CONTACT', meetingMembers);
                })
                .catch(error => {
                    console.log(error.response)
                })
        }
    },
    modules: {
        auth: authModule,
        dashboard: dashboardModule
    }
})
