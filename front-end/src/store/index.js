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
        },
        activeMeeting: '',
        status: null
    },
    getters: {
      getContacts(state) {
          return state.meetingMembers.contacts.map((contact)=>{
               return contact
          });
      },
        getMeeting(state) {
              return state.meetings.map(meeting =>{
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
        },
        ADD_MEETING_ID(state, payload) {
            state.meetingMembers.event_id = payload
        },
        UPDATE_ACTIVE_MEETING(state, payload) {
          state.activeMeeting = payload
        },
        UPDATE_STATUS(state, payload) {
            state.status = payload
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
        async sendRecipients({context}, [meetingMembers, meeting_id]) {
            await axios.post('https://colab8.herokuapp.com/api/events/rsvp', {
                contacts : meetingMembers,
                event_id : meeting_id
            })
                .then(res => {
                    console.log(res.data);
                    context.commit('ADD_MEETING_ID', meeting_id);
                    context.commit('ADD_CONTACT', meetingMembers);
                })
                .catch(error => {
                    console.log(error.response)
                })
        },
        async getMeetingRespound({commit}, id) {
            await axios.get(`https://colab8.herokuapp.com/api/events/rsvp/${id}`)
                .then(res => {
                    commit('UPDATE_ACTIVE_MEETING', res.data)
                })
        },
        async sendRespondStatus({commit}, [payload, id]) {
            await axios.post(`https://colab8.herokuapp.com/api/events/rsvp/${id}`, {
                response : payload,
                rsvp_id : id
            })
                .then(() => {
                    commit('UPDATE_STATUS', payload)
                })
        }
    },
    modules: {
        auth: authModule,
        dashboard: dashboardModule
    }
})
