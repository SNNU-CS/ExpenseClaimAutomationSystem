import Manage from "@/views/workflow/Manage.vue";
import NewWorkflow from "@/views/workflow/NewWorkflow.vue";
import StateSet from "@/views/workflow/StateSet.vue";
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
  },
  {
    path: "workflow/StateSet",
    component: StateSet
  },
  {
    path: "workflow/newstate",
    component: NewWorkflow
  },
];
