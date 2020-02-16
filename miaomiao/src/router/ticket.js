import NewTicket from "@/views/ticket/NewTicket.vue";
import MyTicket from "@/views/ticket/MyTicket.vue";
import TicketDetail from "@/views/ticket/TicketDetail.vue";
import Working from "@/views/ticket/Working.vue";
import Finish from "@/views/ticket/Finish.vue";
export default [
  {
    path: "ticket/new",
    component: NewTicket
  },
  {
    path: "ticket/my",
    component: MyTicket
  },
  {
    path: "ticket/working",
    component: Working
  },
  {
    path: "ticket/all",
    component: Finish
  },
  {
    path: "ticket/detail/:id",
    component: TicketDetail
  }
];
