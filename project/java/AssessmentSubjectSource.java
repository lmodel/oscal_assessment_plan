package None;

/* metamodel_version: 1.7.0 */
/* version: 1.2.1 */
import java.util.List;
import lombok.*;

/**
  Assessment subjects will be identified while conducting the referenced activity.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AssessmentSubjectSource  {

  private String task-uuid;
  private String remarks;

}