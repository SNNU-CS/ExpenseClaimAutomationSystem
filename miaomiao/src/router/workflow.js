import Manage from "@/views/workflow/Manage.vue";
import Workflow from "@/views/workflow/Workflow.vue";
import NewState from "@/views/workflow/NewState.vue";
import StateSet from "@/views/workflow/components/StateSet.vue";
import EditWorkflow from "@/views/workflow/EditWorkflow.vue";
import NewWorkflow from "@/views/workflow/NewWorkflow.vue";
export default [
  {
    path: "workflow",
    component: Workflow
  },
  {
    path: "workflow/edit/:id",
    component: EditWorkflow
  },
  {
    path: "workflow/StateSet",
    component: StateSet
  },
  {
    path: "workflow/newstate",
    component: NewState
  },
  {
    path: "workflow/new",
    component: NewWorkflow
  },
  {
    path: "workflow/manage/:id",
    component: Manage
  },

];
