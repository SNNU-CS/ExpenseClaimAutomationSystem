import axios from 'axios'
import router from '../router'

const api = axios.create({
    baseURL: '/api',
    timeout: 3000,
    // headers: { 'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8' }
    // headers['Content-Type']: 'application/x-www-form-urlencoded;charset=UTF-8'
})

// request
api.interceptors.request.use((config) => {
    console.log(config.headers)
    // if (config.method === 'get') {
    //     config.headers.token = localStorage.token;
    //     // config.headers['X-Token'] = getToken()
    // }
    return config;
}, (error) => {
    return Promise.reject(error);
});

//返回状态判断
api.interceptors.response.use(res => {
    console.log('123');
    // if (!res.data.status && res.data.status !== 0) {
    //     return Promise.reject(res);
    // }
    return res;
}, error => {
    localStorage.username = '';
    localStorage.token = "";
    // router.replace({
    //     path: 'login',
    //     query: { redirect: router.currentRoute.fullPath }
    // });
    // message
    console.log(error.response);
    return Promise.reject(error);
});
export default api