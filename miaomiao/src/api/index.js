import * as auth from "./auth";
import * as user from "./user";
import * as role from "./role";
import * as organization from "./organization";
import * as workflow from "./workflow";
import * as ticket from "./ticket";
export default {
  ...auth,
  ...user,
  ...role,
  ...organization,
  ...workflow,
  ...ticket,
};
