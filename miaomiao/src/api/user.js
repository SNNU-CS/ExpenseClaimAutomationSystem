import request from '@/utils/request'

export function ListUser() {
    return request({
        url: 'account/users/',
        method: 'get'
    })
}
export function DeleteUser(id) {
    return request({
        url: 'account/users/' + id + '/',
        method: 'delete'
    })
}

export function EditUser(id, params) {
    return request({
        url: 'account/users/' + id + '/',
        method: 'put',
        data: params
    })
}
export function AddUser(params) {
    return request({
        url: 'account/users/',
        method: 'post',
        data: params
    })
}