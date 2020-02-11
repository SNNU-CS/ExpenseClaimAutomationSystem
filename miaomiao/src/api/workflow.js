import request from "@/utils/request";

export function ListWorkflow() {
  return request({
    url: "workflow/workflows/",
    method: "get"
  });
}
export function DeleteWorkflow(id) {
  return request({
    url: "workflow/workflows/" + id + "/",
    method: "delete"
  });
}
