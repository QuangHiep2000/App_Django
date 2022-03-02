import axios from 'axios'

axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'
axios.defaults.withCredentials = true

export const BLOG_LIKE_APIS = window.BLOG_LIKE_APIS || {}
export const SLUG = BLOG_LIKE_APIS?.SLUG
export const BASE_URL = BLOG_LIKE_APIS?.BASE_URL
export const GET_BLOG_LIKE_URL = `${BASE_URL}${BLOG_LIKE_APIS?.GET_BLOG_LIKE}`
export const ADD_BLOG_LIKE_URL = `${BASE_URL}${BLOG_LIKE_APIS?.ADD_BLOG_LIKE}`

export function getBlogLikeAPI(){
    return axios.get(`${GET_BLOG_LIKE_URL}?slug=${SLUG}`)
}

export function addBlogLikeAPI(body = {}){
    return axios.post(ADD_BLOG_LIKE_URL, body)
}
