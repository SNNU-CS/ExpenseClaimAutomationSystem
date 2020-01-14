import request from "@/utils/request";

export function ListOrg() {
  return request({
    url: "account/organizations/",
    method: "get"
  });
}
