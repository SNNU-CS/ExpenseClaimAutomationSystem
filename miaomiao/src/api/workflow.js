import request from "@/utils/request";

export function ListTicket() {
  return request({
    url: "workflow/workflows/",
    method: "get"
  });
}
