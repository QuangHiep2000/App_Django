import axios from "axios";

axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'
axios.defaults.withCredentials = true

export const CATEGORY_APIS = window.CATEGORY_APIS || {}
export const BASE_URL = CATEGORY_APIS?.BASE_URL
// export const GET_CATEGORY_URL = `${BASE_URL}${CATEGORY_APIS?.GET_CATEGORY_URL}`
// export const ADD_BLOG_NEW_URL = `${BASE_URL}${CATEGORY_APIS?.ADD_BLOG_NEW_URL}`
export const GET_MY_BLOG_URL = `${BASE_URL}${CATEGORY_APIS?.GET_MY_BLOG_URL}`
export const EDIT_BLOG_NEW_URL = `${BASE_URL}${CATEGORY_APIS?.EDIT_BLOG_NEW_URL}`
export const CHECK_USER_LOGIN = CATEGORY_APIS?.CHECK_USER_LOGIN
export const BLOG_SLUG_URL = CATEGORY_APIS?.BLOG_SLUG_URL
export const SLUG = CATEGORY_APIS?.SLUG


export function getCategoryAPI(){
    return axios.get(`${GET_MY_BLOG_URL}?slug=${SLUG}`)
}

export function addBlogNew(body = {}){
    return axios.put(EDIT_BLOG_NEW_URL, body)
}