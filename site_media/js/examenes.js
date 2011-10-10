$(document).ready(function(){
	var runningRequest = false;
	var request;

	$('select#id_asignatura').change(function(){
		var $id_asign = $(this);

		if($id_asign.val() == ''){
			$('div#resultados').html('');
			return false;
		}

		if(runningRequest){
			request.abort();
		}

		runningRequest=true;
		request = $.getJSON('/archivos/select_ajax',{
			id:$id_asign.val()
		},function(data){
			showResults(data,$id_asign.val());
			runningRequest=false;
		});




		function showResults(data, highlight){
		   var resultHtml = '<table class="tablesorter" border="0" cellpadding="0" cellspacing="0"><thead>';
            resultHtml+='<tr><th class="header headerSortDown"><span>Año</span></th>';
            resultHtml+='<th class="header"><span>Convocatoria</span></th>';
            resultHtml+='<th class="header"><span>Solución<span></span></span></th>';
            resultHtml+='<th class="header"><span>Descargar<span></th></tr></thead><tbody>';

			$.each(data, function(i,item){
				resultHtml+='<tr><td>'+item.anno+'</td>';
                resultHtml+='<td>'+item.convocatoria+'</td>';
                resultHtml+='<td>'+item.solucion+'</td>';
                resultHtml+='<td><a href="'+item.archivo+'"><img src="/site_media/imagenes/download.png" height="25px"/></a><a href="'+item.id+'"><img src="/site_media/imagenes/warning.png" height="25px"/></a></td>';
				resultHtml+='</tr>';
			});
            resultHtml+='</tbody></table>';

			$('div#resultados').html(resultHtml);
		}
	});
});