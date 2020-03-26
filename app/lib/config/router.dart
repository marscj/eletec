import 'package:eletec/view/ad/view.dart';
import 'package:fluro/fluro.dart' as fluro;

import 'package:eletec/view/view.dart';
import 'package:flutter/material.dart';

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
        transition: transition ?? fluro.TransitionType.inFromLeft,
        transitionDuration: transitionDuration,
        transitionBuilder: transitionBuilder);
  }
}
