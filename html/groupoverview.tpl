<?xml version="1.0" encoding="ISO-8859-1"?>

<html xmlns="http://www.w3.org/1999/xhtml">
  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1" />
    <meta http-equiv="Expires" content="now" />
    <meta http-equiv="Cache-Control" content="no-cache" />
    <meta http-equiv="Pragma" content="no-cache" />

    <link href="/OKUSON.css" type="text/css" rel="StyleSheet" />

    <title>�bungsgruppeneinteilung</title>
  </head>

  <body>
    <h1>�bungsgruppeneinteilung</h1>

    <h2>Vorlesung: <CourseName />, <Semester />, <Lecturer /></h2>

    <h3>�bersicht �ber die �bungsgruppen:</h3>

    <p>
    Klicken Sie auf einen Eintrag, um weitere Informationen zu dieser
    Gruppe zu bekommen.
    </p>
    <table>

     <tr><th>Gruppennummer</th> 
         <th>H�rsaal</th>
         <th>Tutor</th>
         <th>Teilnehmerzahl</th></tr>
     <!-- customize with attribute 'components', default is
       components="number,place,tutor,nrparticipants"
       other possible components : time, emailtutor, groupinfo.xxx 
     <GroupsOverview components="number,place,tutor,nrparticipants"/>
    --> <GroupsOverview/>

    </table>

    <hr />

    <h3>Gruppeneinteilung:</h3>
    <p>
    Suchen Sie Ihre Matrikelnummer, um die Nummer Ihrer �bungsgruppe zu
    erfahren.
    </p>
    <table>
      <tr><th>Matrikelnummer</th>
          <th>Gruppennummer</th></tr>

      <GroupDistribution />
 
    </table>
    <hr />

    <p><a href="/index.html">Zur�ck zur Startseite</a></p>

    <p class="foot">Bei Fragen wenden Sie sich bitte an: <br />
      <Feedback /> 
    </p>

    <p class="foot">
      <ValidatorIcon />
    </p>
  </body>
</html>

<!-- Copyright 2003 Frank L�beck and Max Neunh�ffer
     $Id: groupoverview.tpl,v 1.2 2004/03/05 10:40:23 luebeck Exp $ -->

