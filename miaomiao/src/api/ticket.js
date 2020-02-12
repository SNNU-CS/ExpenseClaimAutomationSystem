import request from "@/utils/request";

export function CreateTicket(params) {
  return request({
    url: "workflow/tickets/",
    method: "post",
    data: params
  });
}
