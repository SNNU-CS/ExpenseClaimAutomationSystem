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
export function GetInitState(workflowId) {
  return request({
    url: "workflow/workflows/" + workflowId + "/init_state/",
    method: "get"
  });
}
export function ListWorkflowState(id) {
  return request({
    url: "workflow/workflows/" + id + "/states/",
    method: "get"
  });
}
export function DeleteState(id) {
  return request({
    url: "workflow/states/" + id + "/",
    method: "delete"
  });
}
