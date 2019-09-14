import axios from 'axios'
import router from '../router'
// axios 配置
axios.defaults.timeout = 3000;
axios.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded;charset=UTF-8';
axios.defaults.baseURL = '/api';

//POST传参序列化
axios.interceptors.request.use((config) => {
    if (config.method === 'post') {
        config.headers.token = localStorage.token;
        //
    }
    return config;
}, (error) => {
    return Promise.reject(error);
});

//返回状态判断
axios.interceptors.response.use((res) => {
    if (!res.data.status && res.data.status !== 0) {
        return Promise.reject(res);
    }
    return res;
}, (res) => {
    if (res.response.data.status === 120) {
        localStorage.username = '';
        localStorage.token = "";
        router.replace({
            path: 'login',
            query: { redirect: router.currentRoute.fullPath }
        });
        return Promise.reject(res.response.data.message);
    } else {
        return Promise.reject(res.message);
    }
});

export function fetch(url, params) {
    return new Promise((resolve, reject) => {
        axios.post(url, params)
            .then(response => {
                resolve(response.data);
            }, err => {
                reject(err);
            })
            .catch((error) => {
                reject(error)
            })
    })
}

export function get(url, params) {
    return new Promise((resolve, reject) => {
        axios.get(url, params)
            .then(response => {
                resolve(response.data);
            }, err => {
                reject(err);
            })
            .catch((error) => {
                reject(error)
            })
    })
}


export default {
    Login(params) {
        return get('user/login/', params)
    },
}