import 'package:flutter/material.dart';
// import 'login_card.dart';

class LoginPage extends StatefulWidget {
  @override
  LoginPageState createState() {
    return LoginPageState();
  }
}

class LoginPageState extends State<LoginPage> {
  final scaffoldState = GlobalKey<ScaffoldState>();
  Widget loginScaffold() => Theme(
      data: ThemeData(
          brightness: Brightness.light,
          backgroundColor: Colors.red,
          scaffoldBackgroundColor: Colors.red),
      child: Scaffold(
        key: scaffoldState,
        backgroundColor: Color(0xffeeeeee),
        body: Stack(
          fit: StackFit.expand,
          children: <Widget>[LoginBackground()],
        ),
      ));

  @override
  void initState() {
    super.initState();
  }

  @override
  Widget build(BuildContext context) {
    return loginScaffold();
  }
}

class LoginCard extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return null;
  }
}

class LoginBackground extends StatelessWidget {
  LoginBackground();

  Widget topHalf(BuildContext context) {
    return new Flexible(
      flex: 5,
      child: ClipPath(
        clipper: new ArcClipper(),
        child: Stack(
          children: <Widget>[
            new Container(
              width: double.infinity,
              height: double.infinity,
              decoration: new BoxDecoration(
                  gradient: new LinearGradient(
                begin: Alignment.topCenter,
                end: Alignment.bottomCenter,
                colors: [
                  Colors.black,
                  Colors.blue.shade700,
                ],
              )),
            ),
            new Center(
                child: AspectRatio(
              aspectRatio: 1 / 1,
              child: Image.asset(
                'assets/logo.png',
                fit: BoxFit.none,
                color: Colors.blue,
              ),
            ))
          ],
        ),
      ),
    );
  }

  final bottomHalf = new Flexible(
    flex: 9,
    child: new Container(),
  );

  @override
  Widget build(BuildContext context) {
    return new Flex(
      direction: Axis.vertical,
      children: <Widget>[topHalf(context), bottomHalf],
    );
  }
}

class ArcClipper extends CustomClipper<Path> {
  @override
  Path getClip(Size size) {
    var path = new Path();
    path.lineTo(0.0, size.height - 30);

    var firstControlPoint = new Offset(size.width / 4, size.height);
    var firstPoint = new Offset(size.width / 2, size.height);
    path.quadraticBezierTo(firstControlPoint.dx, firstControlPoint.dy,
        firstPoint.dx, firstPoint.dy);

    var secondControlPoint =
        new Offset(size.width - (size.width / 4), size.height);
    var secondPoint = new Offset(size.width, size.height - 30);
    path.quadraticBezierTo(secondControlPoint.dx, secondControlPoint.dy,
        secondPoint.dx, secondPoint.dy);

    path.lineTo(size.width, 0.0);
    path.close();

    return path;
  }

  @override
  bool shouldReclip(CustomClipper<Path> oldClipper) => false;
}
