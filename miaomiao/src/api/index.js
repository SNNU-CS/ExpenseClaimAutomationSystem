import * as auth from "./auth";
import * as user from "./user";
import * as role from "./role";
import * as organization from "./organization";
export default {
  ...auth,
  ...user,
  ...role,
  ...organization
};
