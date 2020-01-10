import request from "@/utils/request";

export function ListRole() {
  return request({
    url: "account/roles/",
    method: "get"
  });
}
export function DeleteRole(id) {
  return request({
    url: "account/roles/" + id + "/",
    method: "delete"
  });
}

export function UpdateRole(id, params) {
  return request({
    url: "account/roles/" + id + "/",
    method: "put",
    data: params
  });
}
export function CreateRole(params) {
  return request({
    url: "account/roles/",
    method: "post",
    data: params
  });
}
