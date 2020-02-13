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
