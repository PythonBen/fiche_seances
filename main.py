from fasthtml.common import *


app, rt = fast_app()



@rt("/")
def get():
    return Titled("Fiches séances",
                  Div(
                      P(A('waterstart', href='/waterstart')),
                      P(A('tack', href='/tack')),
                  ))

@rt("/waterstart")
def get():
    s1 = " Il s'agit de sortir son corps de l'eau en se servant de la traction de l'aile, et de partir en glisse"
    html_table = """
                    <div class="center">
                <table>
                <thead>
                <tr>
                <th style="text-align: center;">Système </th>
                <th style="text-align: center;">Consignes</th>
                <th style="text-align: center;">Repères </th>
                <th style="text-align: center;">Critères de réussite </th>
                <th style="text-align: center;">Observable </th>
                </tr>
                </thead>
                <tbody>
                <tr>
                <td style="text-align: center;">Aile</td>
                <td style="text-align: center;"> <BR> kite stable à 12h  </td>
                <td style="text-align: center;"> <BR> kite à midi <BR> mouvement rapide de l'aile vers 10h ou 14h <BR> aile bordée</td> </td>
                <td style="text-align: center;"><BR> mouvement rapide <BR> traction générée</td>
                <td style="text-align: center;"> <BR> mouvement rapide </td>
                </tr>
                <tr>
                <td style="text-align: center;">Board</td>
                <td style="text-align: center;"> <BR> planche perpendiculaire aux lignes <BR> équilibrée, gitée (résistance)</td>
                <td style="text-align: center;"><BR> la planche passe du travers , au large</td>
                <td style="text-align: center;"><BR> la planche sort de l'eau avec le vent</td>
                <td style="text-align: center;"> <BR> mouvement fuide <BR> mouvement d'abattée</td>
                </tr>
                <tr>
                <td style="text-align: center;">Rider</td>
                <td style="text-align: center;"> <BR> position fléchie (toilette) <BR> genoux écartés  <BR> appuis talons</td>
                <td style="text-align: center;"><BR> plier les jambes, la jambe avant se tend pour faire abattre la planche </td>
                <td style="text-align: center;"><BR> le rider sort ses fesses de l'eau <BR> pas de catapulte <BR> trajectoire abattue <BR> jambes légèrement pliées  </td>
                <td style="text-align: center;"><BR> mouvement fluide</td>
                </tr>
                <tr>
                
                </tbody>
                </table>
                </div> 
                """


    return (
        Div(
            H1('Waterstart'),
            P(s1),
        P(NotStr(html_table)),
        P(A('Sommaire', href='/')),
        cls="container",
        style="padding-top: 10px;"
           )
         )


@rt("/tack")
def get():
    s1 = "Cette manoeuvre est un demi tour face au vent ou virement de bord. Elle permet de gagner au vent. La clé est un mouvement fluide de l'aile et s'aléger au bon moment"
    html_table = """
                    <div class="center">
                <table>
                <thead>
                <tr>
                <th style="text-align: center;">Système </th>
                <th style="text-align: center;">Consignes</th>
                <th style="text-align: center;">Repères </th>
                <th style="text-align: center;">Critères de réussite </th>
                <th style="text-align: center;">Observable </th>
                </tr>
                </thead>
                <tbody>
                <tr>
                <td style="text-align: center;">Aile</td>
                <td style="text-align: center;"> <BR> kite stable à 11h ou 13h <BR> vitesse <BR> choquer progressivement</td>
                <td style="text-align: center;"> <BR> kite à midi  <BR> aile bordée progressivement</td>
                <td style="text-align: center;"><BR> mouvement continue <BR> sustentation coordonnée à midi</td>
                <td style="text-align: center;"> <BR> mouvement fluide </td>
                </tr>
                <tr>
                <td style="text-align: center;">Board</td>
                <td style="text-align: center;"> <BR> crantage <BR> auloffée</td>
                <td style="text-align: center;"><BR> la planche passe du près, face au vent puis autre amure</td>
                <td style="text-align: center;"><BR> la planche reste à plat</td>
                <td style="text-align: center;"> <BR> mouvement fuide <BR> mouvement de virgule</td>
                </tr>
                <tr>
                <td style="text-align: center;">Rider</td>
                <td style="text-align: center;"> <BR> regard vers le vent <BR> bassin droit <BR> genoux fléchis <BR> appuis talons</td>
                <td style="text-align: center;"><BR> plier les jambes, la jambe avant aide à faire tourner la planche <BR> appui talons</td>
                <td style="text-align: center;"><BR> le rider se suspend au bon moment face au vent <BR> regard déja porté sur l'autre bord <BR> jambes pliées  coordonnées avec l'aile</td>
                <td style="text-align: center;"><BR> mouvement fluide</td>
                </tr>
                <tr>
                
                </tbody>
                </table>
                </div> 
                """
    
    return (
        Div(
            H1('Tack'),
            P(s1),
        P(NotStr(html_table)),
        P(A('Sommaire', href='/')),
        cls="container",
        style="padding-top: 10px;"
           )
         )
serve()