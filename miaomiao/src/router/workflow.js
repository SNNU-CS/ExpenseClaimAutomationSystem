import Manage from "@/views/workflow/Manage.vue";
import Workflow from "@/views/workflow/Workflow.vue";
import NewWorkflow from "@/views/workflow/NewWorkflow.vue";
export default [
  {
    path: "workflow",
    component: Workflow
  },
  {
    path: "workflow/manage/:id",
    component: Manage
  },
  {
    path: "workflow/new",
    component: NewWorkflow
  }
];
