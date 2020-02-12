import Manage from "@/views/workflow/Manage.vue";
import NewWorkflow from "@/views/workflow/NewWorkflow.vue";
export default [
  {
    path: "workflow/manage",
    component: Manage
  },
  {
    path: "workflow/new",
    component: NewWorkflow
  },
  {
    path: "workflow/edit/:id",
    component: NewWorkflow
  }
];
