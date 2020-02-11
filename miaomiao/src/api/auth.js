import request from "@/utils/request";

export function Login(params) {
  return request({
    url: "account/login/",
    method: "post",
    data: params
  });
}
export function SetPassword(id, params) {
  return request({
    url: "account/users/" + id + "/password/",
    method: "post",
    data: params
  });
}
export function GetSelf() {
  return request({
    url: "account/self/",
    method: "get",
  });
}