# -*- coding: ISO-8859-1 -*-
#
#   Okuson extension for entering and editting the results of an exam
#
#   Copyright (C) 2005  Ingo Kl�cker <ingo.kloecker@mathA.rwth-aachen.de>
#
#   This program is free software; you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation; either version 2 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program; if not, write to the Free Software
#   Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

import locale
import Data, Plugins

from fmTools import Utils, AsciiData

class EditExamResults( Plugins.OkusonExtension ):
    state = 0  # this plugin is implemented as finite state machine
    examnr = -1
    options = {}
    maxscore = -1
    scores = {}
    oldscores = {}
    overwrite = {}
    def __init__( self, options = {} ):
        try:
            self.state = int(options['state'][0])
        except:
            self.state = 0
        try:
            self.examnr = int(options['examnr'][0])
        except:
            self.examnr = -1
        self.options = options
        self.scores = {}
        self.oldscores = {}
    def name( self ):
        return self.__class__.__name__
    def necessaryCredentials( self ):
        return Plugins.Admin
    def returnType( self ):
        return Plugins.HTML
    def title( self ):
        return 'Eingabe von Klausurergebnissen'
    def formCode( self ):
        if Data.Exam.maxexamnumber >= 1:
          s = '<input type="hidden" name="state" value="0" />\n'
          s += 'Eingabe der Ergebnisse von Klausur <select name="examnr">\n'
          for i in range( Data.Exam.maxexamnumber ):
            s += ( '<option value="' + str(i) + '">' + str(i) + '</option>\n' )
          s += '</select>\n'
        else:
          s = 'Eingabe von Klausurergebnissen '
          s += '(bislang keine Klausuren eingetragen)\n'
        return s
    def cssCode( self ):
        return '''  table {
                        border          : none;
                        border-collapse : collapse;
                        border-spacing  : 0pt;
                        padding         : 0pt;
                    }
                    th {
                        border        : none;
                        border-left   : 1px solid black;
                        text-align    : left;
                        padding-left  : 15pt;
                        padding-right : 15pt;
                        font-weight   : bold;
                    }
                    th:first-child {
                        border-left   : none;
                    }
                    td {
                        border        : none;
                        border-top    : 1px solid black;
                        border-left   : 1px solid black;
                        text-align    : left;
                        padding-left  : 15pt;
                        padding-right : 15pt;
                        font-weight: normal;
                    }
                    td:first-child {
                        border-left   : none;
                    }'''
    def htmlCode( self ):
        if self.examnr < 0:
            return '<em>Error: Invalid exam number</em>'
        if self.state == 0:
            return self.createExamResultInputMask()
        else:
            errorMsg = self.parseValues()
            if ( errorMsg != None ):
                return errorMsg
            return self.createSummary()

    def parseValues( self ):
        examnr = self.examnr
        # get the maxscore
        maxscore = self.getNumber( 'maxscore' )
        if maxscore == None:
            return '<em>Error: Invalid maximal score.</em>'
        elif maxscore == '':
            return '<em>Error: Missing maximal score.</em>'
        else:
            self.maxscore = maxscore
        # get the individual scores
        self.scores = {}
        self.oldscores = {}
        l = Utils.SortNumerAlpha( Data.people.keys() )
        for k in l:
            p = Data.people[k]
            if ( examnr < len( p.exams ) and p.exams[examnr] != None and
                 p.exams[examnr].registration == 1 ):
                score = self.getNumber( 'P' + str(examnr) + '_' + k, default = -1 )
                if score == None:
                    return '<em>Error: Invalid score for ' + k + '.</em>'
                else:
                    if score > maxscore:
                        return ( '<em>Error: Score for ' + k + ' exceeds the '
                                'maximal score.</em>' )
                    self.scores[k] = [ score,
                                    self.getString( 'S' + str(examnr) + '_' + k ) ]
                    self.oldscores[k] = [ self.getNumber( 'Pold' + str(examnr) + '_' + k,
                                                        default = -1 ),
                                        self.getString( 'Sold' + str(examnr) + '_' + k ) ]

    def createExamResultInputMask( self ):
        examnr = self.examnr
        s = '<h3>Eingabe der Ergebnisse von Klausur ' + str(examnr) + '</h3>\n'
        s += ( '<p><em>Hinweis:</em> Es werden nur diejenigen '
               'Kursteilnehmer angezeigt, die zu dieser Klausur angemeldet '
               'sind.</p>' )
        s += ( '<form action="/AdminExtension" method="post">\n'
               '<div><input type="hidden" name="extension" value="' + 
               self.name() + '" />\n'
               '<input type="hidden" name="state" value="1" />\n'
               '<input type="hidden" name="examnr" value="' +
               str(examnr) + '" /></div>\n' )
        table = []
        table.append( ['', 'Matr.-Nr.', 'Name', 'Punkte', 
                       'Punkte in den einzelnen Aufgaben'] )
        l = Utils.SortNumerAlpha( Data.people.keys() )
        counter = 0
        oldmaxscore = ''
        for k in l:
            p = Data.people[k]
            checked = ''
            if ( examnr < len( p.exams ) and p.exams[examnr] != None ):
                exam = p.exams[examnr]
                if ( exam.maxscore != 0 ):
                    oldmaxscore = locale.str( exam.maxscore )
                if ( exam.registration == 1 ):
                    counter += 1
                    oldtotalscore = ''
                    if ( exam.totalscore != -1 ):
                        oldtotalscore = locale.str( exam.totalscore )
                    table.append( [ str(counter), k,
                                    Utils.CleanWeb( p.lname ) + ', ' +
                                    Utils.CleanWeb( p.fname ),
                                    '<input type="hidden" '
                                    'name="Pold' + str(examnr) + '_' + k + '" '
                                    'value="' + oldtotalscore + '" />'
                                    '<input size="6" maxlength="6" '
                                    'name="P' + str(examnr) + '_' + k + '" '
                                    'value="' + oldtotalscore + '" />',
                                    '<input type="hidden" '
                                    'name="Sold' + str(examnr) + '_' + k + '" '
                                    'value="' + Utils.CleanWeb( exam.scores ) +
                                    '" />'
                                    '<input size="40" maxlength="100" '
                                    'name="S' + str(examnr) + '_' + k + '" '
                                    'value="' + Utils.CleanWeb( exam.scores ) +
                                    '" />' ] )
        s += ( '<p>Maximal erreichbare Punktzahl: '
               '<input name="maxscore" value="' + oldmaxscore + '" '
               'size="4" maxlength="4" /></p>\n' )
        s += createHTMLTable( table )
        s += ( '<p><input type="submit" name="Action" value="Send" />\n'
# Not sure how I can make use of the AdminPasswdField() method. OTOH, this
# method only uses a global variable, so there's no reason for it to be a
# method of a class.
#               '' + handler.AdminPasswdField() + '\n'
               '<input type="password" size="16" maxlength="16" '
               'name="passwd" value="" /></p>\n'
               '</form>\n' )
        return s

    def createSummary( self ):
        examnr = self.examnr
        maxscore = self.maxscore
        scores = self.scores
        oldscores = self.oldscores

        # put the changes into the database
        table = []
        table.append( ['', 'Matr.-Nr.', 'Name', 'Punkte',
                       'Punkte in den einzelnen Aufgaben'] )
        unchanged = []
        unchanged.append( ['', 'Matr.-Nr.', 'Name', 'Punkte (alt)',
                           'Punkte (aktuell)', 'Punkte (Ihre Angabe)',
                           'Details (alt)', 'Details (aktuell)',
                           'Details (Ihre Angabe)'] )
        counter = 0
        unchangedcount = 0
        Data.Lock.acquire()
        for k in Utils.SortNumerAlpha( scores.keys() ):
            p = Data.people[k]
            while len( p.exams ) < examnr + 1:
                p.exams.append( None )
            exam = p.exams[examnr]
            newOrChanged = False
            # we only have to save non-default values for not yet existing
            # entries or changed values for existing entries
            newtotalscore = scores[k][0]
            newdetails = scores[k][1]
            oldtotalscore = oldscores[k][0]
            olddetails = oldscores[k][1]
            # if ( exam == None ):       # only needed for the following print
            #     curtotalscore = -1
            #     curdetails = '<None>'
            # else:
            #     curtotalscore = exam.totalscore
            #     curdetails = exam.scores
            # print ( k + ': totalscore (old/cur/new): ' + str(oldtotalscore) +
            #             '/' + str(curtotalscore) + '/' + str(newtotalscore) +
            #             ' -- details (old/cur/new): "' + olddetails + '"/"' +
            #             curdetails + '"/"' + newdetails + '"' )
            if ( exam == None ):
                # do we have non-default values?
                if ( newtotalscore != -1 or newdetails != '' ):
                    exam = Data.Exam()
                    newOrChanged = True
            else:
                # has the user made changes?
                valuesChanged = ( ( newtotalscore != oldtotalscore ) or
                                  ( newdetails != olddetails ) )
                # are there changes with respect to the currently stored values
                # (because of changes by another user while the first user editted
                # the values)
                needsSaving = ( ( newtotalscore != exam.totalscore ) or
                                ( newdetails != exam.scores ) )
                # have there been changes behind our back
                changedBehindBack = ( ( oldtotalscore != exam.totalscore ) or
                                      ( olddetails != exam.scores ) )
                if ( valuesChanged and needsSaving and changedBehindBack ):
                    # the user has changed a value and additionally this value has
                    # been changed by another user while the first user editted
                    # the values; in this case we don't save our values
                    unchangedcount += 1
                    if newtotalscore == -1:
                        newtotalscorestr = '-'
                    else:
                        newtotalscorestr = locale.str( newtotalscore )
                    if oldtotalscore == -1:
                        oldtotalscorestr = '-'
                    else:
                        oldtotalscorestr = locale.str( oldtotalscore )
                    if exam.totalscore == -1:
                        curtotalscorestr = '-'
                    else:
                        curtotalscorestr = locale.str( exam.totalscore )
                    unchanged.append( [ str(unchangedcount), k,
                                        Utils.CleanWeb( p.lname ) + ', ' +
                                        Utils.CleanWeb( p.fname ),
                                        oldtotalscorestr, curtotalscorestr,
                                        newtotalscorestr, olddetails,
                                        exam.scores, newdetails ] )
                elif ( valuesChanged ):
                    newOrChanged = True
                elif ( exam.maxscore != maxscore and
                       ( oldtotalscore != -1 or olddetails != '' ) ):
                    newOrChanged = True
            if newOrChanged:
                exam.totalscore = newtotalscore
                exam.scores = newdetails
                exam.maxscore = maxscore
                line = AsciiData.LineTuple( ( k, str(examnr), str(newtotalscore),
                                              str(maxscore), newdetails ) )
                try:
                    Data.examdesc.AppendLine( line )
                except:
                    Data.Lock.release()
                    Utils.Error( '[' + Utils.LocalTimeString() +
                                 '] Failed to store exam result:\n' + line )
                    return '<em>Error: The results could not be saved.</em>'
                p.exams[examnr] = exam
                counter += 1
                if newtotalscore == -1:
                    newtotalscorestr = '-'
                else:
                    newtotalscorestr = locale.str( newtotalscore )
                table.append( [ str(counter), k,
                                Utils.CleanWeb( p.lname ) + ', ' +
                                Utils.CleanWeb( p.fname ),
                                newtotalscorestr,
                                newdetails ] )
        Data.Lock.release()

        Utils.Error( '[' + Utils.LocalTimeString() + '] Changed results '
                     'for exam ' + str(examnr),
                     prefix = self.name() + ': ' )
        s = '<h3>Ergebnisse von Klausur ' + str(examnr) + '</h3>\n'
        if len(unchanged) > 1:
            s += ( '<p>Einige Werte wurden ge�ndert, w�hrend Sie die Werte editiert '
                   'haben. Daher wurden die folgenden �nderungen <strong>nicht</strong> '
                   'gespeichert.' )
            s += createHTMLTable( unchanged )
        s += '<p>Die folgenden �nderungen wurden gespeichert.</p>'
        s += createHTMLTable( table )
        return s

    def getNumber( self, optionName, default = '' ):
        ''' Returns the number corresponding to the query option @p optionName
            or returns an empty string if the query option does not exist or is
            empty (except for possible whitespace) or returns None if the value
            of the query option is no valid number.'''
        if optionName not in self.options:
            return default
        # allow the usage of ',' instead of '.' for decimal numbers
        s = self.options[optionName][0].strip().replace( ',', '.' )
        if s == '':
            return default
        t = 0
        try:
            if '.' in s:
                t = float( s )
            else:
                t = int( s )
        except:
            return None
        return t

    def getString( self, optionName ):
        if optionName not in self.options:
            return ''
        return self.options[optionName][0]

    def headAndBody( self ):
        pass

def createHTMLTable( table, className = None ):
    if className == None:
        s = '<table>\n<thead>\n'
    else:
        s = '<table class="' + className + '">\n<thead>\n'
    # first row is table head
    s += '<tr>'
    for cell in table[0]:
        s += '<th>' + cell + '</th>'
    s += '</tr>\n'
    s += '</thead>\n<tbody>\n'
    for row in table[1:]:
        s += '<tr>'
        for cell in row:
            s += '<td>' + cell + '</td>'
        s += '</tr>\n'
    s += '</tbody>\n</table>\n'
    return s

Plugins.register( EditExamResults.__name__,
                  'Klausuren',
                  'Eingabe von Klausurergebnissen',
                  'Dieses Plugin erlaubt die Eingabe von Klausurergebnissen.',
                  'Ingo Kl�cker',
                  'Ingo Kl�cker',
                  '2005',
                  EditExamResults )
