import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import reportWebVitals from './reportWebVitals';
// import CreateBlog from "./components/CreateBlog";
import EditBlog from "./components/EditBlog";

// ReactDOM.render(
//   <React.StrictMode>
//     <CreateBlog />
//   </React.StrictMode>,
//   document.getElementById('create_new_blog')
// );

ReactDOM.render(
  <React.StrictMode>
    <EditBlog />
  </React.StrictMode>,
  document.getElementById('edit_new_blog')
);


// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
