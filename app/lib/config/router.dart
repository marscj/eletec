import 'package:eletec/view/ad/view.dart';
import 'package:fluro/fluro.dart' as fluro;

import 'package:eletec/view/view.dart';

class Routes {
  static String root = '/';
  static String home = '/home';
  static String login = '/login';

  static void configureRoutes(fluro.Router router) {
    router.define(root,
        handler: fluro.Handler(handlerFunc: (_, __) => AdPage()));
    router.define(home,
        handler: fluro.Handler(handlerFunc: (_, __) => HomePage()));
  }
}

class Router {
  fluro.Router router;

  static Router get instance => Router._();

  Router._() {
    router = fluro.Router();
    Routes.configureRoutes(router);
  }
}
