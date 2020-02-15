import request from "@/utils/request";

export function CreateTicket(params) {
  return request({
    url: "workflow/tickets/",
    method: "post",
    data: params
  });
}
export function UploadTicketFile(files) {
  return request({
    url: "workflow/tickets/upload/",
    method: "post",
    data: files
  });
}
export function ListTicket(params) {
  return request({
    url: "workflow/tickets/",
    method: "get",
    params: params
  });
}
export function DeleteTicket(id) {
  return request({
    url: "workflow/tickets/" + id + "/",
    method: "delete"
  });
}
export function DetailTicket(id) {
  return request({
    url: "workflow/tickets/" + id + "/",
    method: "get"
  });
}
export function TicketLogs(ticketId) {
  return request({
    url: "workflow/tickets/" + ticketId + "/flowlogs/",
    method: "get"
  });
}
export function TicketTransitions(ticketId) {
  return request({
    url: "workflow/tickets/" + ticketId + "/transitions/",
    method: "get"
  });
}
export function TicketStep(ticketId) {
  return request({
    url: "workflow/tickets/" + ticketId + "/steps/",
    method: "get"
  });
}
