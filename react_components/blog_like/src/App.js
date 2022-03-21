// import logo from './logo.svg';
import './App.css';
import React, {useState, useEffect} from 'react';
import toast, {Toaster} from 'react-hot-toast';
import axios from 'axios'
import {addBlogLikeAPI, getBlogLikeAPI, SLUG, CHECK_USER_LOGIN} from "./api";
// import {StyledButton} from './/styles/StyledButton';
import tw, {styled, theme, css} from 'twin.macro';

axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'
axios.defaults.withCredentials = true


function App() {
    const [dataLike, setDataLike] = useState({});
    const [checkLike, setCheckLike] = useState(false)
    const [countLike, setCountLike] = useState(0)

    const StyledButton = styled.div(({checkLike}) =>[
        checkLike ? (tw`text-white bg-gradient-to-br from-green-400 to-blue-600 font-medium rounded-lg text-sm px-4 py-3 text-center flex justify-center items-center cursor-pointer opacity-50`)
             : tw`text-white bg-gradient-to-br from-green-400 to-blue-600 hover:bg-gradient-to-bl focus:ring-4 focus:ring-green-200 dark:focus:ring-green-800 font-medium rounded-lg text-sm px-4 py-3 text-center flex justify-center items-center cursor-pointer`,
    ]);

    // const notify = () => ;toast('Here is your toast.')
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
                if (res.data.ok) {
                    setDataLike(res.data.data);
                    setCheckLike(res.data.data.isLiked);
                    setCountLike(res.data.data.totalLikes);
                }
            })
            .catch(() => {
            })

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
            if (CHECK_USER_LOGIN) {
                await addBlogLikeAPI({
                    slug: SLUG
                })
                setCountLike(countLike + 1)
                setCheckLike(true)
                toast.success('Like is success!')
            } else {
                toast.error("You not Login!")
            }
        }
    }
    return (<div className="App">
        <div className={"container-like"}>
            <div><Toaster
                position="top-center"
                reverseOrder={false}
            /></div>
            <div className={"total-like"}>Lượt thích: {dataLike && countLike}</div>
            <StyledButton onClick={handleClick} checkLike={checkLike}>
                like
                <i className={"bi bi-hand-thumbs-up-fill icon-like"}></i>
            </StyledButton>
        </div>
    </div>);
}

export default App;
