import { CKEditor } from '@ckeditor/ckeditor5-react';
import ClassicEditor from '@ckeditor/ckeditor5-build-classic';
// import 'flowbite';
import {getCategoryAPI, addBlogNew, CHECK_USER_LOGIN, BLOG_SLUG_URL, BASE_URL, SLUG} from "./api";
import React, {useState, useEffect} from "react";
import toast, {Toaster} from 'react-hot-toast';
import InputLabel from '@mui/material/InputLabel';
import MenuItem from '@mui/material/MenuItem';
import Select from '@mui/material/Select';
import FormControl from '@mui/material/FormControl';
// import 'twin.macro'


function App() {
    const [dataCategory, setDataCategory] = useState([])
    const [dataTitle, setDataTitle] = useState('')
    const [dataSelect, setDataSelect] = useState('')
    const [dataContent, setDataContent] = useState('')
    const [isMyBlog, setIsMyBlog] = useState(null)

    useEffect(() =>{
        getCategoryAPI()
            .then(res =>{
                if(res.data.ok){
                    console.log(res.data)
                    setDataCategory(res.data.data.category)
                    setDataSelect(res.data.data.currentCategory)
                    setDataTitle(res.data.data.title)
                    setDataContent(res.data.data.content)
                    setIsMyBlog(res.data.isMyBlog)
                }
            })
    }, [])
    function renderCategory(){
        return dataCategory.map((item, index) =>{
            return <MenuItem key={index} value={item.name}>{item.name}</MenuItem>
        })
    }


    async function handlSubmit(event){
        event.preventDefault()
        if(CHECK_USER_LOGIN){
            let checkSubmit = true
            if(dataTitle.trim().length < 3){
                toast.error("Title không được nhỏ hơn 3 ký tự!")
                checkSubmit = false
            }
            else if(dataTitle.trim().length > 200){
                toast.error("Title không được lớn hơn 200 ký tự!")
                checkSubmit = false
            }
            else if(dataSelect === ''){
                toast.error("Chưa chọn category")
                checkSubmit = false
            }
            else if(dataContent.trim().length < 20){
                toast.error("Nội dung không được nhỏ hơn 20 ký tự!")
                checkSubmit = false
            }
            else if(dataContent.trim().length > 3000){
                toast.error("Nội dung không được lớn hơn 3000 ký tự!")
                checkSubmit = false
            }
            else if(checkSubmit){
                await addBlogNew({
                    title: dataTitle.trim(),
                    category: dataSelect,
                    content: dataContent,
                    slug: SLUG,
                }).then(res =>{
                    setTimeout(() =>{
                        window.location.href = `${BASE_URL}${BLOG_SLUG_URL}${SLUG}`
                    }, 2000)
                })
                toast.success("Edit Blog Success")
            }
        }
        else {
            toast.error("You not Login!")
        }
    }

    function handleTitle(e){
        setDataTitle(e.target.value)
    }

    function handleSelect(e){
        setDataSelect(e.target.value)
    }

    function checkIsMyBlog(){
        if(isMyBlog === true){
            return <>
                <div className="shadow-lg w-4/5 p-8 bg-white rounded-lg">
                    <div><Toaster
                        position="top-center"
                        reverseOrder={false}
                    /></div>
                    <form className="">
                        <div className="relative z-0 mb-6 group">
                            <input onChange={(e) => handleTitle(e)} type="text" name="floating_email"
                                   className="block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-b-2 border-gray-300 appearance-none dark:text-black dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer"
                                   placeholder=" " required
                                   defaultValue={dataTitle}
                            />
                            <label htmlFor="floating_email"
                                   className="absolute mb-2 text-sm text-gray-500 dark:text-gray-400 duration-300 transform -translate-y-6 scale-75 top-3 -z-10 origin-[0] peer-focus:left-0 peer-focus:text-blue-600 peer-focus:dark:text-blue-500 peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-6">
                                Title</label>
                        </div>
                        <FormControl variant="standard" sx={{ m: 1, minWidth: 120 }}>
                            <InputLabel id="demo-simple-select-standard-label">Category</InputLabel>
                            <Select
                                className="w-40"
                                labelId="demo-simple-select-standard-label"
                                id="demo-simple-select-standard"
                                // open={open}
                                // onClose={handleClose}
                                // onOpen={handleOpen}
                                value={dataSelect}
                                label="Category"
                                onChange={handleSelect}
                            >
                                {renderCategory()}
                            </Select>
                        </FormControl>
                        <div onChange={handleSelect} className="relative z-0 mb-4 mt-10 w-full group">
                            {/*<select className="text-white bg-gradient-to-r from-cyan-500 to-blue-500 hover:bg-gradient-to-bl focus:ring-4 focus:ring-cyan-300 dark:focus:ring-cyan-800 font-medium rounded-lg text-sm px-5 py-2.5 text-center mr-2 mb-2 w-100" name="floating_password">*/}
                            {/*    <option>Thể loại truyện</option>*/}
                            {/*    {renderCategory()}*/}
                            {/*</select>*/}
                            {/*<label htmlFor="floating_password"*/}
                            {/*       className="absolute text-lg text-gray-500 dark:text-gray-400 duration-300 transform -translate-y-6 scale-75 -top-2 left-0 -z-10 origin-[0] peer-focus:left-0 peer-focus:text-blue-600 peer-focus:dark:text-blue-500 peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-6">*/}
                            {/*    Category</label>*/}
                        </div>
                        <div className="m-h-96">
                            <p className="text-sm text-gray-500 dark:text-gray-400 mb-2">Content</p>
                            <CKEditor
                                id={""}
                                editor={ ClassicEditor }
                                data={dataContent}
                                onChange={ ( event, editor ) => {
                                    const data = editor.getData();
                                    setDataContent(data)
                                } }
                            />
                        </div>
                        <button onClick={handlSubmit} type="submit"
                                className="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm w-full sm:w-auto px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800 mt-2">Thay đổi
                        </button>
                    </form>
                </div>

            </>
        }
        else if(isMyBlog === false) {
            return <>
                <div id="alert-additional-content-2" className="p-4 mb-4 bg-red-100 rounded-lg dark:bg-red-200"
                     role="alert">
                    <div className="flex items-center">
                        <svg className="mr-2 w-5 h-5 text-red-700 dark:text-red-800" fill="currentColor"
                             viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                            <path fill-rule="evenodd"
                                  d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7-4a1 1 0 11-2 0 1 1 0 012 0zM9 9a1 1 0 000 2v3a1 1 0 001 1h1a1 1 0 100-2v-3a1 1 0 00-1-1H9z"
                                  clip-rule="evenodd"></path>
                        </svg>
                        <h3 className="text-lg font-medium text-red-700 dark:text-red-800">This is a danger alert</h3>
                    </div>
                    <div className="mt-2 mb-4 text-sm text-red-700 dark:text-red-800">
                        Bạn không có quyền truy cập trang này
                    </div>
                    <div className="flex">
                        {/*<button type="button"*/}
                        {/*        className="text-white bg-red-700 hover:bg-red-800 focus:ring-4 focus:ring-red-300 font-medium rounded-lg text-xs px-3 py-1.5 mr-2 text-center inline-flex items-center dark:bg-red-800 dark:hover:bg-red-900">*/}
                        {/*    <svg className="-ml-0.5 mr-2 h-4 w-4" fill="currentColor" viewBox="0 0 20 20"*/}
                        {/*         xmlns="http://www.w3.org/2000/svg">*/}
                        {/*        <path d="M10 12a2 2 0 100-4 2 2 0 000 4z"></path>*/}
                        {/*        <path fill-rule="evenodd"*/}
                        {/*              d="M.458 10C1.732 5.943 5.522 3 10 3s8.268 2.943 9.542 7c-1.274 4.057-5.064 7-9.542 7S1.732 14.057.458 10zM14 10a4 4 0 11-8 0 4 4 0 018 0z"*/}
                        {/*              clip-rule="evenodd"></path>*/}
                        {/*    </svg>*/}
                        {/*    View more*/}
                        {/*</button>*/}
                        <a className="color-transparent no-underline" href="/">
                            <button type="button"
                                className="text-red-700 border border-red-700 hover:bg-red-800 hover:text-white focus:ring-4 focus:ring-red-300 font-medium rounded-lg text-xs px-3 py-1.5 text-center dark:border-red-800 dark:text-red-800 dark:hover:text-white"
                                data-collapse-toggle="alert-additional-content-2" aria-label="Close">
                                Về trang chủ
                            </button>
                        </a>
                    </div>
                </div>
            </>
        } else return null
    }

    return (
        <div className="AppCreateNewBlog bg-gradient-to-r from-purple-500 to-pink-500">

            <div className="container mx-auto px-6 h-screen flex items-center justify-center">
                {checkIsMyBlog()}


            </div>
        </div>
    );
}

export default App;