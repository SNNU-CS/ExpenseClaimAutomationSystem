import request from '@/utils/request'

export default {
    Login(params) {
        return request({
            url: 'account/login/',
            method: 'post',
            params: params
        })
    }
}