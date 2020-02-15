import Manage from "@/views/workflow/Manage.vue";
import Workflow from "@/views/workflow/Workflow.vue";
import NewState from "@/views/workflow/components/NewState.vue";
import StateSet from "@/views/workflow/components/StateSet.vue";
import NewWorkflow from "@/views/workflow/NewWorkflow.vue";
import FlowChart from "@/views/workflow/FlowChart.vue";
export default [
  {
    path: "workflow",
    component: Workflow
  },
  {
    path: "workflow/StateSet",
    component: StateSet
  },
  {
    path: "workflow/:id/state/new",
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
  {
    path: "workflow/:id/flow-chart",
    component: FlowChart
  }
  // {
  //   path: "workflow/:id/trans/new",
  //   component: NewState
  // },
  // {
  //   path: "workflow/:id/fields/new",
  //   component: NewState
  // }
];
