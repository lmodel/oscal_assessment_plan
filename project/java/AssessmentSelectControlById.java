package None;

/* metamodel_version: 1.7.0 */
import java.util.List;
import lombok.*;

/**
  Select a specific control for inclusion/exclusion in the assessment by literal control ID and optional statement IDs.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AssessmentSelectControlById  {

  private String control-id;
  private List<String> statement-ids;

}