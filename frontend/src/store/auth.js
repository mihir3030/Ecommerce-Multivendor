import { create } from 'zustand'
import { mountStoreDevtool } from 'simple-zustand-devtools'


// set for update state. get for getting current data
const useAuthStore = create((set, get) => ({
    allUserdata: null,
    loading: false,

    // get user info
    user: () => ({
        user_id: get().allUserdata?.user_id || null,
        username: get().allUserdata?.username || null,
    }),

    // when call replace old with new user data
    setUser: (user) => set({ allUserdata: user }),
    setLoading: (loading) => set({ loading }),
    isLoggedIn: () => get().allUserdata !== null

}))

if (import.meta.env.DEV) {
    mountStoreDevtool('Store', useAuthStore)
}

export { useAuthStore }