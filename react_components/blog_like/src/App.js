// import logo from './logo.svg';
import './App.css';
import React, {useState, useEffect} from 'react';
import axios from 'axios'
import {addBlogLikeAPI, getBlogLikeAPI, SLUG} from "./api";

axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'
axios.defaults.withCredentials = true


function App() {
    const [dataLike, setDataLike] = useState({});
    const [checkLike, setCheckLike] = useState(false)
    const [countLike, setCountLike] = useState(0)
    // function getCookie(name) {
    //     if (!document.cookie) {
    //         return null;
    //     }
    //
    //     const xsrfCookies = document.cookie.split(';')
    //         .map(c => c.trim())
    //         .filter(c => c.startsWith(name + '='));
    //
    //     if (xsrfCookies.length === 0) {
    //         return null;
    //     }
    //     return decodeURIComponent(xsrfCookies[0].split('=')[1]);
    // }

    useEffect(() => {
        getBlogLikeAPI()
            .then(res => {
                if (res.data.ok){
                    setDataLike(res.data.data);
                    setCheckLike(res.data.data.isLiked);
                    setCountLike(res.data.data.totalLikes);
                }
            })
            .catch(() => {})

        // axios({
        //     method: 'GET', url: `${window.BLOG_LIKE_API.BASE_URL}${window.BLOG_LIKE_API.GET_BLOG_LIKE}`,
        //
        // })
        //     .then(function (response) {
        //         // response.data.pipe(fs.createWriteStream('ada_lovelace.jpg'))
        //         setDataLike(response.data);
        //         setCheckLike(response.data.isLiked);
        //         setCountLike(response.data.totalLikes);
        //     });
    }, [])

    async function handleClick() {
        if (!checkLike) {
            // axios({
            //     method: 'POST', url: `${window.BLOG_LIKE_API.BASE_URL}${window.BLOG_LIKE_API.ADD_BLOG_LIKE}`, data: {
            //         is_liked: true, slug: window.BLOG_LIKE_API.SLUG, user: dataLike.user
            //     }
            // });

            await addBlogLikeAPI({
                 slug: SLUG
            })
            setCountLike(countLike + 1)
            setCheckLike(true)
        }
    }

    return (<div className="App">
        <div className={"container-like"}>
            <div className={"total-like"}>Lượt thích: {dataLike && countLike}</div>
            <div onClick={handleClick}
                 className={"like" + (checkLike ? " class_is_liked" : "")}>like <i
                className={"bi bi-hand-thumbs-up-fill icon-like"}></i></div>
        </div>
    </div>);
}

export default App;
