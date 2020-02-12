import NewTicket from "@/views/ticket/NewTicket.vue";
import MyTicket from "@/views/ticket/MyTicket.vue";
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
    component: MyTicket
  },
  {
    path: "ticket/finish",
    component: MyTicket
  }
];
