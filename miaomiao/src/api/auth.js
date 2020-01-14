import request from "@/utils/request";

export function Login(params) {
  return request({
    url: "account/login/",
    method: "post",
    data: params
  });
}
