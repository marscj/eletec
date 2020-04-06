import 'package:fluro/fluro.dart' as fluro;
import 'package:flutter/material.dart';

import 'package:eletec/view/view.dart';

class Routes {
  static String root = '/home';
  static String home = '/';
  static String login = '/login';

  static void configureRoutes(fluro.Router router) {
    router.define(root,
        handler: fluro.Handler(handlerFunc: (_, __) => AdPage()));
    router.define(home,
        handler: fluro.Handler(handlerFunc: (_, __) => Home()));
  }
}

class Router extends fluro.Router {
  static Router get instance => Router._();

  Router._() {
    Routes.configureRoutes(this);
  }

  @override
  Future navigateTo(BuildContext context, String path,
      {bool replace = false,
      bool clearStack = false,
      fluro.TransitionType transition,
      Duration transitionDuration = const Duration(milliseconds: 250),
      RouteTransitionsBuilder transitionBuilder}) {
    return super.navigateTo(context, path,
        replace: replace,
        clearStack: clearStack,
        transition: transition ?? fluro.TransitionType.cupertino,
        transitionDuration: transitionDuration,
        transitionBuilder: transitionBuilder);
  }
}
