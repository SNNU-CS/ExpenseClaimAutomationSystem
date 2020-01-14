import axios from "axios";
import router from "../router";
import { Message } from "element-ui";
const api = axios.create({
  baseURL: "/api",
  timeout: 3000,
  headers: { "Content-Type": "application/json;charset=UTF-8" }
  // headers['Content-Type']: 'application/x-www-form-urlencoded;charset=UTF-8'
});

// request
api.interceptors.request.use(
  (config) => {
    if (localStorage.Token !== undefined) {
      config.headers["Authorization"] = "Bearer" + " " + localStorage.Token;
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

//返回状态判断
api.interceptors.response.use(
  (res) => {
    if (res.data.status !== 200) {
      // can user a table{status:type} in the future
      Message({
        message: res.data.msg,
        type: "error"
      });
      // return Promise.reject(res.data.msg);
      return new Promise(() => {});
    } else {
      return res.data;
    }
  },
  (error) => {
    if (error.response.status === 401) {
      localStorage.clear();
      Message({
        message: "当前用户没有登录!",
        type: "error"
      });
      // router.replace({
      //     path: 'login',
      //     query: { redirect: router.currentRoute.fullPath }
      // });
    } else if (error.response.status === 500) {
      Message({
        message: "服务器内部错误!",
        type: "error"
      });
    }
    return Promise.reject(error);
  }
);
export default api;
