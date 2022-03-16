import { createStore } from 'vuex'

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
            context.commit('ADD_MEETING', meeting);
        }
    },
    modules: {}
})
